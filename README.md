# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 399
- HTTP: 113 alive / 76 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 173 alive / 152 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48073
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
