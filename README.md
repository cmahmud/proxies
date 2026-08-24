# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 423
- HTTP: 156 alive / 76 gold
- HTTPS: 96 alive / 21 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33854
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
