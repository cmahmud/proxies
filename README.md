# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 407
- HTTP: 112 alive / 61 gold
- HTTPS: 131 alive / 19 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41365
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
