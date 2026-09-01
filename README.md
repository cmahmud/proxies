# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 445
- HTTP: 96 alive / 76 gold
- HTTPS: 95 alive / 28 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47362
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
