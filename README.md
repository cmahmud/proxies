# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 410
- HTTP: 97 alive / 72 gold
- HTTPS: 36 alive / 17 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48249
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
