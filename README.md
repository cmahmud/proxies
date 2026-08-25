# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 418
- HTTP: 116 alive / 74 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34879
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
