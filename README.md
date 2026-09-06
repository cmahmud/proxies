# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 407
- HTTP: 104 alive / 73 gold
- HTTPS: 57 alive / 22 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48096
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
