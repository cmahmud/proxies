# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 409
- HTTP: 143 alive / 74 gold
- HTTPS: 90 alive / 18 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 192 alive / 159 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33778
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
