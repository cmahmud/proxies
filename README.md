# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 398
- HTTP: 76 alive / 56 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36761
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
