# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 424
- HTTP: 99 alive / 66 gold
- HTTPS: 56 alive / 20 gold
- SOCKS4: 187 alive / 166 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48899
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
