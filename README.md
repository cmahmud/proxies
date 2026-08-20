# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 380
- HTTP: 227 alive / 60 gold
- HTTPS: 101 alive / 20 gold
- SOCKS4: 191 alive / 149 gold
- SOCKS5: 205 alive / 151 gold

## Historical pool

- Discovered: 146663
- Ever alive: 25741
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
