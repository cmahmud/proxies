# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 380
- HTTP: 95 alive / 46 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33540
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
