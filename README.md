# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 384
- HTTP: 123 alive / 50 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33535
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
