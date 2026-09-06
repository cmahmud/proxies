# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 390
- HTTP: 97 alive / 68 gold
- HTTPS: 45 alive / 17 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 171 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48188
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
