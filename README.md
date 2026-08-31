# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 481
- HTTP: 136 alive / 102 gold
- HTTPS: 122 alive / 43 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45077
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
