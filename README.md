# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 479
- HTTP: 157 alive / 102 gold
- HTTPS: 127 alive / 42 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44972
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
