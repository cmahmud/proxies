# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 437
- HTTP: 131 alive / 77 gold
- HTTPS: 117 alive / 24 gold
- SOCKS4: 191 alive / 163 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47620
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
