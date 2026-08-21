# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 427
- HTTP: 329 alive / 95 gold
- HTTPS: 242 alive / 27 gold
- SOCKS4: 229 alive / 144 gold
- SOCKS5: 266 alive / 161 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28182
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
