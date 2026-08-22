# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 402
- HTTP: 234 alive / 93 gold
- HTTPS: 166 alive / 29 gold
- SOCKS4: 181 alive / 123 gold
- SOCKS5: 245 alive / 157 gold

## Historical pool

- Discovered: 167131
- Ever alive: 32552
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
