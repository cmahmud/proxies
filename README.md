# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 385
- HTTP: 115 alive / 63 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 186 alive / 154 gold
- SOCKS5: 194 alive / 157 gold

## Historical pool

- Discovered: 175416
- Ever alive: 33129
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
