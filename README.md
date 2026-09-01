# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 478
- HTTP: 147 alive / 100 gold
- HTTPS: 127 alive / 38 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 194 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46946
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
