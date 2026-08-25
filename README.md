# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 414
- HTTP: 96 alive / 60 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36239
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
