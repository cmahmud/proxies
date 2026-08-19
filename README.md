# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 526
- HTTP: 350 alive / 153 gold
- HTTPS: 265 alive / 105 gold
- SOCKS4: 224 alive / 143 gold
- SOCKS5: 201 alive / 125 gold

## Historical pool

- Discovered: 127374
- Ever alive: 19949
- Ever gold: 806

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
