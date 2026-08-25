# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 406
- HTTP: 106 alive / 66 gold
- HTTPS: 74 alive / 21 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34978
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
