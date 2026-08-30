# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 481
- HTTP: 158 alive / 102 gold
- HTTPS: 123 alive / 42 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44974
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
