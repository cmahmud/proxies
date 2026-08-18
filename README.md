# SyndProxy private pool

## Current pool

- Alive now: 623
- Gold now: 212
- HTTP: 163 alive / 26 gold
- HTTPS: 92 alive / 7 gold
- SOCKS4: 164 alive / 97 gold
- SOCKS5: 204 alive / 82 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
