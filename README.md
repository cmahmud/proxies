# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 425
- HTTP: 100 alive / 66 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 184 alive / 167 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48901
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
