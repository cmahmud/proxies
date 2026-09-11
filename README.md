# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 337
- HTTP: 142 alive / 77 gold
- HTTPS: 87 alive / 30 gold
- SOCKS4: 84 alive / 53 gold
- SOCKS5: 286 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48564
- Ever gold: 1545

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
