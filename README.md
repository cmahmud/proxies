# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 412
- HTTP: 106 alive / 71 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33712
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
