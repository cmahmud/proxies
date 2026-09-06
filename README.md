# SyndProxy validated proxy pool

## Current pool

- Alive now: 406
- Gold now: 320
- HTTP: 82 alive / 54 gold
- HTTPS: 32 alive / 12 gold
- SOCKS4: 147 alive / 133 gold
- SOCKS5: 145 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48332
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
