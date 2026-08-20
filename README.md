# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 393
- HTTP: 266 alive / 87 gold
- HTTPS: 186 alive / 19 gold
- SOCKS4: 212 alive / 144 gold
- SOCKS5: 200 alive / 143 gold

## Historical pool

- Discovered: 144823
- Ever alive: 25322
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
