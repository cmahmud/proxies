# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 369
- HTTP: 90 alive / 45 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 177 alive / 154 gold
- SOCKS5: 195 alive / 157 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32958
- Ever gold: 1219

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
