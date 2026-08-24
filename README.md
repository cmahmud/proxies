# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 382
- HTTP: 127 alive / 65 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 176 alive / 151 gold
- SOCKS5: 185 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33225
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
