# SyndProxy private pool

## Current pool

- Alive now: 1455
- Gold now: 623
- HTTP: 539 alive / 206 gold
- HTTPS: 443 alive / 115 gold
- SOCKS4: 231 alive / 144 gold
- SOCKS5: 242 alive / 158 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24039
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
