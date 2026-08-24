# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 413
- HTTP: 120 alive / 72 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33752
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
