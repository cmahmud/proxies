# SyndProxy private pool

## Current pool

- Alive now: 860
- Gold now: 414
- HTTP: 248 alive / 97 gold
- HTTPS: 171 alive / 30 gold
- SOCKS4: 225 alive / 144 gold
- SOCKS5: 216 alive / 143 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31763
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
