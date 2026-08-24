# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 407
- HTTP: 149 alive / 73 gold
- HTTPS: 94 alive / 17 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33777
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
