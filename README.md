# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 470
- HTTP: 143 alive / 95 gold
- HTTPS: 122 alive / 35 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46329
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
