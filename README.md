# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 440
- HTTP: 96 alive / 71 gold
- HTTPS: 103 alive / 31 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 183 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47446
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
