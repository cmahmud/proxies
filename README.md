# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 477
- HTTP: 151 alive / 97 gold
- HTTPS: 124 alive / 41 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46954
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
