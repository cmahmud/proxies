# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 469
- HTTP: 147 alive / 91 gold
- HTTPS: 116 alive / 41 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46967
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
