# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 410
- HTTP: 109 alive / 69 gold
- HTTPS: 169 alive / 13 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41213
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
