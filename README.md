# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 425
- HTTP: 130 alive / 74 gold
- HTTPS: 113 alive / 24 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35035
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
