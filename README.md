# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 455
- HTTP: 128 alive / 89 gold
- HTTPS: 106 alive / 33 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44794
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
