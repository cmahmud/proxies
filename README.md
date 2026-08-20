# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 382
- HTTP: 229 alive / 73 gold
- HTTPS: 128 alive / 18 gold
- SOCKS4: 193 alive / 145 gold
- SOCKS5: 210 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25834
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
