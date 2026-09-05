# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 310
- HTTP: 119 alive / 76 gold
- HTTPS: 32 alive / 19 gold
- SOCKS4: 88 alive / 71 gold
- SOCKS5: 177 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1487

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
