# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 412
- HTTP: 97 alive / 65 gold
- HTTPS: 72 alive / 22 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37776
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
