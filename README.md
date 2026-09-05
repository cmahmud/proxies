# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 302
- HTTP: 131 alive / 73 gold
- HTTPS: 33 alive / 17 gold
- SOCKS4: 102 alive / 68 gold
- SOCKS5: 181 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1482

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
