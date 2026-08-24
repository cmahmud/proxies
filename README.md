# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 384
- HTTP: 92 alive / 47 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33543
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
