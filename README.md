# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 412
- HTTP: 86 alive / 58 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36263
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
