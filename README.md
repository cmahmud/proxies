# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 387
- HTTP: 117 alive / 63 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 177 alive / 158 gold

## Historical pool

- Discovered: 175416
- Ever alive: 33129
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
