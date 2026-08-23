# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 347
- HTTP: 225 alive / 38 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 181 alive / 154 gold
- SOCKS5: 221 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32869
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
