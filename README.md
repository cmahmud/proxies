# SyndProxy validated proxy pool

## Current pool

- Alive now: 456
- Gold now: 361
- HTTP: 75 alive / 43 gold
- HTTPS: 43 alive / 8 gold
- SOCKS4: 164 alive / 154 gold
- SOCKS5: 174 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33018
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
