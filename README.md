# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 407
- HTTP: 118 alive / 71 gold
- HTTPS: 54 alive / 14 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33276
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
