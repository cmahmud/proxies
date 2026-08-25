# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 412
- HTTP: 86 alive / 58 gold
- HTTPS: 73 alive / 20 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36265
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
